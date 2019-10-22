import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  userInfo: "",
  postList: [],
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
    }))

    commit('setMovieSearchList', movies)
  },

  async signUp({ commit }, params) {
    console.log("enter addMember!!")
    await api.signUp(params)
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
  },

  async getnoticedetail({commit}, params){
    console.log('여기는 store/data.js')
    const resp = await api.getnoticedetail(params)
    const summary = {
        title: resp.data.title,
        content: resp.data.content
    }
    return summary
    // commit('setSummary', summary)
  },

  async noticeupdate({commit}, params){
    console.log(params)
    await api.updatenotice(params)
  },

  async DeleteNotice({commit}, params){
    console.log('여기는 store/data.js 삭제중')
    console.log(params)
    await api.deletenotice(params)
  },

  async DeleteBoard({commit}, params){
    console.log('여기는 store/data.js 삭제중')
    console.log(params)
    await api.deleteboard(params)
  },
}

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m)
  },
  printUserInfo(state, user) {
    state.userInfo = user.map(m => m)
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations,
}