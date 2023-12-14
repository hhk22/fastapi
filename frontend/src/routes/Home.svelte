<script>
    import fastapi from "../lib/api.js";
    import { link } from "svelte-spa-router";

    let question_list = [];

    function get_question_list() {
        fastapi("get", "/api/question/list", {}, (json) => {
            question_list = json;
        });
    }

    get_question_list();
</script>

<ul>
    <h1>Question List</h1>
    {#each question_list as question}
        <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
    {/each}
</ul>
