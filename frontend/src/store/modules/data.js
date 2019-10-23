import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  userInfo: "",
  userPage: true, 
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

  async getAllNotices(){
    return await api.getAllNotices()
  },

  async noticeWrite({commit}, params){
    await api.noticeWrite(params)
  },

  async getAllBoards(){
    return await api.getAllBoards()
  },

  async boardWrite({commit}, params){
    await api.boardWrite(params)
  },

  async getBoardDetail({commit}, params){
    const resp = await api.getBoardDetail(params)
    const summary = {
        title: resp.data.title,
        content: resp.data.content
    }
    return summary
    // commit('setSummary', summary)
  },

  async getNoticeDetail({commit}, params){
    const resp = await api.getNoticeDetail(params)
    const summary = {
        title: resp.data.title,
        content: resp.data.content
    }
    return summary
    // commit('setSummary', summary)
  },

  async noticeUpdate({commit}, params){
    console.log(params)
    await api.updateNotice(params)
  },

  async boardUpdate({commit}, params){
    await api.updateBoard(params)
  },

  async DeleteNotice({commit}, params){
    await api.deleteNotice(params)
  },

  async DeleteBoard({commit}, params){
    await api.deleteBoard(params)
  },
}

// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m)
  },
  printUserInfo(state, user) {
    state.userInfo = user.map(m => m)
  },
}

export default {
  namespaced: true,
  state,
  actions,
  mutations,
}