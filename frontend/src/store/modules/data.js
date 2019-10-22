import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  userInfo: "",
  postList: [],
}

// actions
const actions = {
  async signUp({ commit }, params) {
    console.log("enter addMember!!")
    await api.signUp(params)
  },
  async checkLogin({ commit }, params) {
    console.log("enter checkLogin!!")
    return await api.checkLogin(params).then((result) => {
      var resp = result.data
      console.log("resp : " + resp.favorite)
      if(resp.is_authenticated){
        var user={
          username: resp.username,
          token: resp.token,
          is_staff: resp.is_staff,
        }
        commit('setUser', user)
        localStorage.setItem("token", state.user.token)
        return true
      }else{
        return false
      }
    });
  },
  async getAllUsers() {
    return await api.getAllUsers()
  },
  async getallnotices(){
    return await api.getallnotices()
  },

  async noticewrite({commit}, params){
    await api.noticewrite(params)
  },

  async getallboards(){
    var a = await api.getallboards()
    console.log('data.js')
    console.log(a)
    return a
  },

  async boardwrite({commit}, params){
    console.log('월요일')
    console.log(params)
    console.log("data.js까지 왔음")
    await api.boardwrite(params)
  },

  async getboarddetail({commit}, params){
    console.log('여기?')
    const resp = await api.getboarddetail(params)
    console.log(resp)
    const summary = {
        title: resp.data.title,
        content: resp.data.content
    }
    return summary
    // commit('setSummary', summary)
  }
}

// mutations
const mutations = {
  printUserInfo(state, user) {
    state.userInfo = user.map(m => m)
  },
  setUser(state, user) {
    state.user = user
  },

}

export default {
  namespaced: true,
  state,
  actions,
  mutations,
}