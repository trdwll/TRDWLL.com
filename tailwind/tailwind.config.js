module.exports = {
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    extend: {
      minWidth: {
        '2': '2rem',
      },
      maxWidth: {
        '2': '2rem',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
  purge: {
    enabled: true, //true for production build
    preserveHtmlElements: false,
    content: [
      '../templates/**/*.html',
    ],
    options: {
      safelist: ['dark', /^text-(red|blue|gray|green)-500/, /^border-gray-(300|700)/, 'bg-gray-200', 'border-solid', 'border-collapse'],
      keyframes: true,
      fontFace: true,
    }
  },
}