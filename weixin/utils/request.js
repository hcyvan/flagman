const env = require('../config/env.js')
const server = `${env.serverProtocol}://${env.serverHost}`
const header = {
  'content-type': 'application/json'
}
const request = function (api, method='GET', data=null) {
  return new Promise(function(resolve, reject){
    let params = {
      url: `${server}${api}`,
      method: method,
      header: header,
      success: resolve,
      fail: reject,
    }
    if (data) {
      params.data=data
    }
    wx.request(params)
  })
}

const _get = function(api, data=null) {
  return request(api, 'GET', data)
}

const _post = function (api) {
  return request(api, 'POST')
}

const _put = function(api) {
  return request(api, 'PUT')
}

const _delete = function (api) {
  return request(api, 'DELETE')
}

module.exports = {
  get: _get,
  post: _post,
  put: _put,
  delete: _delete,
}
