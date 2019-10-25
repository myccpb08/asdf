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
    return axios.get(`${apiUrl}/allNotices/`).then((result) => {
      return result.data
    });
  },

  getNoticeComments(params){
    return axios.get(`${apiUrl}/getNoticeComments/`,{params}).then((result) => {
      return result.data
    });
  },

  getBoardComments(params){
    return axios.get(`${apiUrl}/getBoardComments/`,{params}).then((result) => {
      return result.data
    });
  },

  noticeWrite(params){
    return axios.post(`${apiUrl}/notice/`, {
      params,
    })
  },

  noticeCommentWrite(params){
    console.log(653)
    return axios.post(`${apiUrl}/noticeComment/`, {
      params,
    })
  },

  getAllBoards() {
    return axios.get(`${apiUrl}/allBoards/`).then((result) => {
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

  boardCommentWrite(params){
    console.log(653)
    return axios.post(`${apiUrl}/boardComment/`, {
      params,
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

  deleteBoardComment(params){
    return axios.delete(`${apiUrl}/boardComment/`, 
    { params})
  },

  deleteNoticeComment(params){
    return axios.delete(`${apiUrl}/noticeComment/`, 
    { params})
  },

  editBoardComment(params){
    return axios.put(`${apiUrl}/boardComment/`, 
    { params})
  },

  editNoticeComment(params){
    return axios.put(`${apiUrl}/noticeComment/`, 
    { params})
  }
}