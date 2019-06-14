import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Course from '@/components/Course'
import Detail from '@/components/Detail'
import Micro from '@/components/Micro'
import News from '@/components/News'
import Login from '@/components/Login'
import Help from '@/components/help/Help'
import AboutUs from '@/components/help/AboutUs'
import Feedback from '@/components/help/Feedback'
import UserNote from '@/components/help/UserNote'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/index',
      name: 'index',
      component: Index
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: Detail,
      meta: {
        requireAuth: true
      }

    },
    {
      path: '/micro',
      name: 'micro',
      component: Micro
    },
    {
      path: '/news',
      name: 'news',
      component: News
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/help',
      name: 'help',
      component: Help,
      children: [
        {
          path: 'about-us',
          name: 'about-us',
          component: AboutUs
        },
        {
          path: 'user-note',
          name: 'user-note',
          component: UserNote
        },
        {
          path: 'feedback',
          name: 'feedback',
          component: Feedback
        }
      ]
    }
  ],
  mode: "history"
})
