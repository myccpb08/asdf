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
    return a
  },

  async boardwrite({commit}, params){
    await api.boardwrite(params)
  },

  async getboarddetail({commit}, params){
    const resp = await api.getboarddetail(params)
    const summary = {
        title: resp.data.title,
        content: resp.data.content
    }
    return summary
    // commit('setSummary', summary)
  },

  async getnoticedetail({commit}, params){
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

  async boardupdate({commit}, params){
    await api.updateboard(params)
  },

  async DeleteNotice({commit}, params){
    await api.deletenotice(params)
  },

  async DeleteBoard({commit}, params){
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