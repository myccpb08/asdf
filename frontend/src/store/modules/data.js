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
  async signUp({ commit }, params) {
    console.log("enter addMember!!")
    await api.signUp(params)
  },
  async getAllUsers() {
    return await api.getAllUsers()
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