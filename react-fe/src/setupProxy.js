const proxy = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api/v1/backend',
    proxy({
      target: 'http://localhost:3001',
      pathRewrite: {
        '^/api/v1/backend': '' // remove base path
      },
    })
  );
};
