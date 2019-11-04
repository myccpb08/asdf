import axios from 'axios'

const apiUrl = '/api'

export default {
  signUp(params) {
    return axios.post(`${apiUrl}/auth/signup/`, {
      user: params,
    })
  },
  async checkLogin(params) {
    return await axios.post(`${apiUrl}/auth/checkLogin/`, {
      username: params.username,
      password: params.password
    })
  },
  async checkPassword(params) {
    return await axios.post(`${apiUrl}/auth/checkPassword/`, {
      username: params.username,
      inputPass: params.inputPass
    })
  },
  async editUser(params) {
    await axios.put(`${apiUrl}/auth/user/`, {
      username: params.username,
      name: params.name,
      password: params.password,
      favorite: params.favoriteValue,
      grade: params.grade
    })
  },
  async deleteUser(params) {
    console.log(params)
    return axios.delete(`${apiUrl}/auth/user/`, 
    {params})
  },
  async logoutUser(param) {
    return await axios.post(`${apiUrl}/auth/logout/`, {
        username: param
    })
  },
  async getSession(param) {
      return await axios.post(`${apiUrl}/auth/session/`, {
          token: param
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
    console.log(params)
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
  },

  getService(params){
    return axios.get(`${apiUrl}/getService/`,{params}).then((result) => {
      return result.data
    });
  },

  policySearch(params){
    return axios.get(`${apiUrl}/policySearch/`,{params}).then((result) => {
      return result.data
    });
  },

  policySearchByWord(params){
    return axios.get(`${apiUrl}/policySearchByWord/`,{params}).then((result) => {
      return result.data
    });
  }
}