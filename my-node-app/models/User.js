// models/User.js
const db = require('../config/database');

class User {
  constructor(id, username, email, password) {
    this.id = id;
    this.username = username;
    this.email = email;
    this.password = password;
  }

  static async create(username, email, password) {
    const sql = `
      INSERT INTO users (username, email, password)
      VALUES (?, ?, ?);
    `;
    const result = await db.run(sql, [username, email, password]);
    return new User(result.lastID, username, email, password);
  }

  static async findByUsername(username) {
    const sql = `
      SELECT * FROM users
      WHERE username = ?;
    `;
    const result = await db.get(sql, [username]);
    return result ? new User(result.id, result.username, result.email, result.password) : null;
  }
}

module.exports = User;