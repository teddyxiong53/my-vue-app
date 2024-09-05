// app.js
const express = require('express');
const app = express();
const authRouter = require('./routes/auth');

app.use(express.json());
app.use('/api/auth', authRouter);

const port = 5000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});