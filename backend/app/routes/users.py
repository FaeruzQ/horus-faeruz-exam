from flask import Blueprint, request, jsonify
from ..services.user_service import UserService
from ..utils.validators import is_valid_email
from ..extensions import jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ..models.user import User
from ..extensions import db

users_bp = Blueprint("users", __name__)

@users_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    nama = data.get("nama")

    if not all([username, password, email, nama]):
        return jsonify({"message": "Wajib diisi semua"}), 400

    if not is_valid_email(email):
        return jsonify({"message": "Format email tidak valid"}), 400

    # check uniqueness
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username sudah ada"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email sudah terdaftar"}), 400

    user = UserService.create_user(username, password, email, nama)
    return jsonify({"message": "Registrasi berhasil"}), 201

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    if not all([username, password]):
        return jsonify({"message": "Username dan password wajib diisi"}), 400
    
    user = UserService.authenticate(username, password)
    if not user:
        return jsonify({"message": "Username atau password salah"}), 401
    
    access_token = create_access_token(identity=str(user.id))  
    return jsonify({"message": "Login berhasil", "token": access_token}), 200

@users_bp.route("", methods=["GET"])
@jwt_required()
def get_users():
    users = UserService.get_all_users()
    return jsonify([u.to_dict() for u in users]), 200

@users_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User tidak ditemukan"}), 404
    return jsonify(user.to_dict()), 200

@users_bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    data = request.get_json() or {}
    username = data.get("username")
    email = data.get("email")
    nama = data.get("nama")

    if not all([username, email, nama]):
        return jsonify({"message": "Wajib diisi semua"}), 400

    if not is_valid_email(email):
        return jsonify({"message": "Format email tidak valid"}), 400

    other = User.query.filter(User.id != user_id).filter((User.username == username) | (User.email == email)).first()
    if other:
        return jsonify({"message": "Username atau email sudah dipakai oleh user lain"}), 400

    user = UserService.update_user(user_id, username, email, nama)
    if not user:
        return jsonify({"message": "User tidak ditemukan"}), 404

    return jsonify({"message": "Data user berhasil diperbarui"}), 200

@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    success = UserService.delete_user(user_id)
    if not success:
        return jsonify({"message": "User tidak ditemukan"}), 404
    return jsonify({"message": "User berhasil dihapus"}), 200