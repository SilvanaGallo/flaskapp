<h1 class="mb-0 h3">Flask app</h1>
<main id="main" aria-label="Content">
        
<div class="xblock xblock-student_view xblock-student_view-vertical xblock-initialized" data-course-id="course-v1:Jobandtalent+PY101+202210" data-init="VerticalStudentView" data-runtime-class="LmsRuntime" data-runtime-version="1" data-block-type="vertical" data-usage-id="block-v1:Jobandtalent+PY101+202210+type@vertical+block@38bd59aad3e94e5d8a1d67f49a67eb74" data-request-token="1057ae2270cc11edbff90242ac12000b" data-graded="False" data-has-score="False">
  
<div class="vert-mod">
    <div class="vert vert-0" data-id="block-v1:Jobandtalent+PY101+202210+type@html+block@edfbdbac62714722ae1553278b5f8524">
        
<div class="xblock xblock-student_view xblock-student_view-html xmodule_display xmodule_HtmlBlock xblock-initialized" data-course-id="course-v1:Jobandtalent+PY101+202210" data-init="XBlockToXModuleShim" data-runtime-class="LmsRuntime" data-runtime-version="1" data-block-type="html" data-usage-id="block-v1:Jobandtalent+PY101+202210+type@html+block@edfbdbac62714722ae1553278b5f8524" data-request-token="1057ae2270cc11edbff90242ac12000b" data-graded="False" data-has-score="False">
  
<p>The application consists in an <strong>integration of a 3rd party API Rollbar</strong> (error tracking platform). The backend have 2 different interfaces (API Rest and CLI), both interfaces run the same use cases.</p>

<h3>Tasks during the project</h3>

<h4>1. Preparing of the environment</h4>
<p>All the infrastructure services must be managed by Docker / Docker compose (databases, etc.).</p>
<p>There are 2 files Dockerfile and docker-compose.yml to construct the image and setup the database for running</p>
<p>We're using <strong>Python 3.10.6</strong> version, and <code>pyenv</code> to manage this requirement.</p>
<p>In addition, we're using <strong>pip</strong> to install and manage dependencies and packages (you can find the requirements.txt file with all dependencies and versions for this project).</p>
<p>Finally, we use <strong>dotenv</strong> to manage secrets and keys. You can find an .env file example with all required credentials and data.</p>

<h4>2. Basic routes</h4>
<p>Our Flask application have 2 basic routes:</p>
<ul>
<ul>
<li><strong><code>/which</code></strong> that returns a text message, for example "API under construction".</li>
<li><strong><code>/check</code></strong> that is the health check of the application and returns a JSON about it:</li>
</ul>
</ul>
<p></p>
<!-- HTML generated using hilite.me -->
<div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0px; line-height: 125%;">{
    <span style="color: #000080;">"status"</span>: <span style="color: #bb8844;">"OK" or "KO" (depending on the database connection status)</span>
}
</pre>
</div>
<!--end snippet-->
<p></p>

<h4>3. API</h4>
<p>There is an API implemented in flask with all the operations <strong>(create, update, delete, show and list items)</strong> in order to interact with Rollbar. The following endpoints are available in the application to manage the message items:</p>
<table width="80%">
<tbody>
<tr>
<td>GET (all)</td>
<td>
<p>/items</p>
</td>
</tr>
<tr>
<td>GET (one item by id)</td>
<td>
<p>/items/:id</p>
</td>
</tr>
<tr>
<td>POST (one item)</td>
<td>
<p>/items</p>
</td>
</tr>
<tr>
<td>PUT | PATCH (one item by id)</td>
<td>
<p>/items/:id</p>
</td>
</tr>
<tr>
<td>DELETE</td>
<td>
<p>/items/:id</p>
</td>
</tr>
</tbody>
</table>

<h4>4. Reports</h4>
<p>We have a PostgreSQL database to store reports. You can use the /reports to access the stored information and to clean reports.</p>
<p>Reports are stored in a JSON format, in order to retrieve the same information that Rollbar.</p>
<p>The following endpoints are available in the application to manage this reports:</p>
<table width="80%">
<tbody>
<tr>
<td>GET</td>
<td>
<p>/reports</p>
</td>
</tr>
<tr>
<td>DELETE</td>
<td>
<p>/reports</p>
</td>
</tr>
</tbody>
</table>

<h4>5. CLI</h4>
<p>The service can be executed also via <strong>CLI</strong>. That interface is implemented with <strong>click</strong> and it is available in cli.py file.</p>
<p> Use <strong> python cli.py --help</strong> to see the commands and arguments.</p>

<h4>6. Instrument your application with Datadog</h4>
<p>I had problems with DataDog client execution. I don't know if it is a problem with amazon linux or if it is a conflict between ports.</p>

<h4>7. Bonus</h4>
<ul>
<ul>
<li><strong>Implement pagination in the list endpoints.</strong> Not implemented yet.</li>
<li><strong>Update the code of your <code>/check</code> endpoint to return&nbsp;<strong>KO</strong>when the connection with the database is broken.</strong> I added a try except block into the endpoint to test the connection by doing a simple select query and, if it raises an exception, I can assume that there is a problem with the database connection </li>
<li><strong>Handle the credentials using environment variables, do not put the secrets in the code.</strong> I started using a Config class to capture the credentials from the environment variables os the OS. Then I installed dotenv but I had doubts about where set the values from the .env file</li>
</ul>
</ul>
<p></p>
</div>

    </div>
</div>


  
  <script type="text/javascript">
    (function (require) {
        require(['/static/js/dateutil_factory.a28baef97506.js?raw'], function () {
          require(['js/dateutil_factory'], function (DateUtilFactory) {
            
    DateUtilFactory.transform('.localized-datetime');

          });
        });
    }).call(this, require || RequireJS.require);
  </script>


<script>
    function emit_event(message) {
        parent.postMessage(message, '*');
    }
</script>

</div>

      </main>
