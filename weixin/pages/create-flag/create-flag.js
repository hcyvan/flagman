Page({
  data: {
    addressName: '',
    address: '',
    addressLocation: {},
    flagTime: '',
    flagDate: '',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  chooseLocation: function () {
    var that = this
    wx.chooseLocation({
      success: function (res) {
        console.log(res)
        that.setData({
          'addressName': res.name,
          'address': res.address,
          'addressLocation.latitude': res.latitude,
          'addressLocation.longitude': res.longitude,
        })
      }
    })
  },
  
  bindDateChange: function (e) {
    console.log(e)
    this.setData({
      flagDate: e.detail.value
    })
  },

  bindTimeChange: function (e) {
    this.setData({
      flagTime: e.detail.value
    })
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