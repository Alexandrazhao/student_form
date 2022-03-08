import Vue from 'vue'
import App from './App.vue'
// import axios
import axios from 'axios'

Vue.config.productionTip = false
// set a prototype for http
Vue.prototype.$http = axios;
new Vue({
  render: h => h(App),
}).$mount('#app')
