Page({
  data: {
    result: null
  },
  onSubmit(e) {
    const { year, month, day, hour } = e.detail.value;
    wx.request({
      url: 'http://localhost:8000/fortune',
      data: { year, month, day, hour },
      success: res => {
        this.setData({ result: res.data });
      }
    });
  }
});
