import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Course from "./views/Course.vue";
import ModType from "./views/ModType.vue";
import Industry from "./views/Industry.vue";
import About from "./views/About.vue";
import Module from "@/components/ModulePage.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/home",
      name: "home",
      component: Home
    },
    {
      path: "/course",
      name: "course",
      component: Course
    },
    {
      path: "/modtype",
      name: "modtype",
      component: ModType
    },
    {
      path: "/industry",
      name: "industry",
      component: Industry
    },
    {
      path: "/about",
      name: "about",
      component: About
    },
    {
      path: "/module",
      name: "module",
      component: Module,
      props: true
    },
  ]
});
