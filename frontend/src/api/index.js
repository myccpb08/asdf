import axios from 'axios'

const apiUrl = '/api'

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params,
    })
  },
  signUp(params) {
    return axios.post(`${apiUrl}/auth/signup/`, {
      user: params,
    })
  },
  getAllUsers() {
    return axios.get(`${apiUrl}/auth/allUsers/`).then((result) => {
      return result.data
    });
  },

  getAllNotices(){
    return axios.get(`${apiUrl}/allnotices/`).then((result) => {
      return result.data
    });
  },

  noticeWrite(params){
    return axios.post(`${apiUrl}/notice/`, {
      params,
    })
  },

  getAllBoards() {
    return axios.get(`${apiUrl}/allboards/`).then((result) => {
      return result.data
    });
  },

  updateNotice(params){
    axios.post(`${apiUrl}/noticeDetail/`, {
      params
    })
  },

  updateBoard(params){
    axios.post(`${apiUrl}/boardDetail/`, {
      params
    })
  },

  boardWrite(params){
    console.log('api index.js')
    return axios.post(`${apiUrl}/board/`, {
      params,
    })
  },

  getBoardDetail(params) {
    console.log('api폴더 getboarddetail')
    return axios.get(`${apiUrl}/boardDetail/`, {
        params
    })
  },
  
  getNoticeDetail(params) {
    console.log('api폴더 getnoticedetail')
    return axios.get(`${apiUrl}/noticeDetail/`, {
        params
    })
  },

  deleteNotice(params) {
    console.log('삭제옵니까?')
    console.log(params)
    return axios.delete(`${apiUrl}/noticeDetail/`, 
    { params})
  },

  deleteBoard(params) {
    return axios.delete(`${apiUrl}/boardDetail/`, 
    { params})
  },
}