import { createRouter, createWebHistory } from 'vue-router'

// Import views
const Home = () => import('@/views/Home.vue')
const Menu = () => import('@/views/Menu.vue')
const Reservations = () => import('@/views/Reservations.vue')
const About = () => import('@/views/About.vue')
const Contact = () => import('@/views/Contact.vue')

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { title: "Kurdie's Curry" }
  },
  {
    path: '/menu',
    name: 'Menu',
    component: Menu,
    meta: { title: 'Our Menu' }
  },
  {
    path: '/reservations',
    name: 'Reservations',
    component: Reservations,
    meta: { title: 'Book Your Table' }
  },
  {
    path: '/about',
    name: 'About',
    component: About,
    meta: { title: 'About Us' }
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact,
    meta: { title: 'Contact Us' }
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// Navigation guards
router.beforeEach((to, from, next) => {
  console.log('Navigating from:', from.path, 'to:', to.path)
  next()
})

export default router
