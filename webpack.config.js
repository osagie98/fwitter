const path = require('path');

module.exports = {
  entry: './fwitter/js/fwitter.jsx',
  mode: 'development',
  output: {
    path: path.join(__dirname, '/fwitter/static/js/'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        use:
          {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env'],
            }
          }
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};
