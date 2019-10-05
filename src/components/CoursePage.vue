<template>
  <div class="course_page">
    <div>
      <b-card
        overlay
        img-src="https://images.pexels.com/photos/159213/hall-congress-architecture-building-159213.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
        img-alt="Card Image"
        text-variant="white"
        title="Course"
        title-tag="h1"
        img-height="350px"
      >
        <b-card-text>
          Find out when your seniors are taking their modules. Are you taking a module too early?
        </b-card-text>
      </b-card>
      </div>
    <b-container fluid class="content">
      </br>
      <CourseDataTable/>
      <br/><br/>
    </b-container>
    <Footer/>
  </div>
</template>

<script>
  import Footer from "@/components/Footer.vue";
  import {module_enrolment} from '../firebase';
  import CourseDataTable from "@/components/CourseDataTable.vue";

  export default {
    name: "course",
    data() {
      return {
        items: []
      }
    },
    firebase: {
      items: module_enrolment
    },
    components: {
      CourseDataTable,
      Footer
    },
  };
</script>

<style scoped>
.titlePosition {
  color: #003d7c;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: "bold";
  font-size: 56px;
  width: 100%;
  text-align: center;
  margin-top: 50px;
  padding-bottom: 0px;
}

.moduleTitle {
  color: #003d7c;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: "bold";
  font-size: 56px;
  width: 100%;
  text-align: center;
  margin-top: 0px;
  margin-left: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
}

.shiftLeft {
  padding-right: 15px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

/* ---------CSS for banner------------- */
.card-img{
  object-fit:cover;
  object-position:center;
  filter: brightness(40%);
}
h1{
  color:white;
  margin-top:7rem;
  font-size:4rem;
}
.cart-text{
  font-size:2rem;
}

</style>
