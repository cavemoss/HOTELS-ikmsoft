/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './templates/**/*.html',
    './static/**/*.css',
  ],
  theme: {
    extend: {
      borderWidth: {
        '1.5': '1.5px',
      },
    },
  },
  plugins: [],
}
