import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  userInfo: "",
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
  async addMember({ commit }, params) {
    alert("enter addMember!!")
    const resp = await api.addMember(params)
    console.log(resp)
    const user = resp.data.map(d => ({
      id: d.id,
      userid: d.userid,
      username: d.username,
      password: d.password,
    }))
    commit('printUserInfo', user)
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