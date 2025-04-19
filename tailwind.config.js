// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.html",
    "./scriptapp/templates/**/*.html",
    "./**/*.py", // optional, only needed if you use classes in Python files
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
