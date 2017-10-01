// pages/main/main.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    location: {},
    controls: [{
      id: 1,
      iconPath: "/images/flagdog_to_replace.png",
      position: {},
      clickable: true
    }],
    markers: [{
      iconPath: "/images/pin.png",
      id: 1,
      latitude: 23.099994,
      longitude: 113.324520,
      width: 50,
      height: 50
    }]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.initControlsPosition()
    wx.getLocation({
      type: 'gcj02',
      success: res => {
        let latitude = res.latitude
        let longitude = res.longitude
        this.setData({
          'location.latitude': latitude,
          'location.longitude': longitude,
          'markers[0].latitude': latitude,
          'markers[0].longitude': longitude,
        })

        var speed = res.speed
        var accuracy = res.accuracy
      }
    })
  },

  initControlsPosition: function() {
    var res = wx.getSystemInfoSync()
    let logoWidth = res.windowWidth / 3
    this.setData({
      'controls[0].position.top': res.windowHeight - logoWidth / 2,
      'controls[0].position.left': res.windowWidth / 2 - logoWidth / 2,
      'controls[0].position.width': logoWidth,
      'controls[0].position.height': logoWidth,
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})