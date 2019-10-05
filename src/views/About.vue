<template>
  <div class="about">
    <AboutPage/>
  </div>
</template>

<script>
// @ is an alias to /src
import AboutPage from "@/components/AboutPage.vue";

export default {
  name: "about",
  components: {
    AboutPage
  }
};
</script>