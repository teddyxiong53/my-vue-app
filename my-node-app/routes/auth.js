// routes/auth.js
const express = require('express');
const router = express.Router();
const User = require('../models/User');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

router.post('/register', async (req, res) => {
  const { username, email, password } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);
  const user = await User.create(username, email, hashedPassword);
  res.send(`User created successfully: ${user.username}`);
});

router.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await User.findByUsername(username);
  if (!user) {
    return res.status(401).send('Invalid username or password');
  }
  const isValid = await bcrypt.compare(password, user.password);
  if (!isValid) {
    return res.status(401).send('Invalid username or password');
  }
  const token = jwt.sign({ userId: user.id }, process.env.SECRET_KEY, {
    expiresIn: '1h',
  });
  res.send({ token });
});

module.exports = router;