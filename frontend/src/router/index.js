import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import PredView from "../views/PredView.vue";
import ResearchView from "../views/ResearchView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/pred",
    name: "pred",
    component: PredView,
  },
  {
    path: "/our-research",
    name: "Our Research",
    component: ResearchView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
