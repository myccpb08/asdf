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

  async getAllNotices(){
    return await api.getAllNotices()
  },

  async noticeWrite({commit}, params){
    await api.noticeWrite(params)
  },

  async noticeCommentWrite({commit}, params){
    await api.noticeCommentWrite(params)
  },

  async boardCommentWrite({commit}, params){
    await api.boardCommentWrite(params)
  },

  async getNoticeComments({commit}, params){
    return await api.getNoticeComments(params)
  },

  async getBoardComments({commit}, params){
    return await api.getBoardComments(params)
  },

  async getAllBoards(){
    var a = await api.getAllBoards()
    return a
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

  async deleteBoardComment({commit}, params){
    await api.deleteBoardComment(params)
  },

  async deleteNoticeComment({commit}, params){
    await api.deleteNoticeComment(params)
  },

  async editBoardComment({commit}, params){
    await api.editBoardComment(params)
  },

  async editNoticeComment({commit}, params){
    await api.editNoticeComment(params)
  }
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