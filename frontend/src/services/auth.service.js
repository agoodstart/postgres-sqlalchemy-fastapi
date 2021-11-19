import axios from 'axios'

const API_URL = 'http://localhost:8000/api/v1/auth';

class AuthService {
    login(user) {
        return axios
            .post(API_URL + '/login', {
                username: user.admin_email,
                password: user.admin_password
            })
            .then(response => {
                if(response.data.accessToken) {
                    localStorage.setItem('admin', JSON.stringify(response.data))
                }

                return response.data
            });
    }

    logout() {
        localStorage.removeItem('admin')
    }

    register(admin) {
        return axios.post(API_URL + '/signup', {
            admin_email: admin.admin_email,
            admin_passowrd: admin.admin_password
        })
    }
}

export default new AuthService();