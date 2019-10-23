import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  userInfo: "",
  postList: [],
  user: null,
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
      if(resp.is_authenticated){
        var user={
          username: resp.username,
          favorite: resp.favorite,
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
  async logoutUser({ commit }) {
      await api.logoutUser(state.user.username).then(() => {
          localStorage.removeItem("token");
          commit('setUser', null);
      })
  },
  async getSession({ commit }, param) {
    return await api.getSession(param).then((result) => {
      if (result.data.is_authenticated) {
        commit('setUser', {
          username: result.data.username,
          favorite: result.data.favorite,
          token: result.data.token,
          is_staff: result.data.is_staff,
        })
      } else {
        localStorage.removeItem('token');
        commit('setUser', null);
      }
      return result.data.is_authenticated;
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