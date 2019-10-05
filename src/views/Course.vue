<template>
  <div class="course">
    <CoursePage/>
  </div>
</template>

<script>
// @ is an alias to /src
import CoursePage from "@/components/CoursePage.vue";

export default {
  name: "course",
  components: {
    CoursePage
  }
};
</script>