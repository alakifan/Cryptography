# Cryptography

<h3>Qué es y para qué sirve</h3>
<p> Cryptography es un paquete que provee de <a href="https://en.wikipedia.org/wiki/Cryptographic_primitive">primitivas criptográficas</a> (algoritmos criptográficos de bajo nivel) a desarrolladores Python para añadir seguridad a sus programas. Aspira a ser la librería estándar de criptografía.</p>
<h4>Instalación</h4>
<p>Es muy simple, se puede hacer con pip con el comando:</p>
<pre><span class="gp">$</span> pip install cryptography</pre>
<h4>Disposición</h4>
<p>Cryptography está dividido en dos niveles, uno con fórmulas criptográficas de fácil uso que prácticamente no requieren que el desarrollador tome muchas decisiones, y otro con primitivas criptográficas de bajo nivel. Estas suelen ser peligrosas y pueden ser usadas incorrectamente. Requieren toma de decisiones y un conocimiento profundo en el campo de la criptografía. Debido al potencial peligro que suponen, nos referimos a ellas como el nivel de "Materiales peligrosos".</p>

<h3>Principales módulos</h3>
<h4>Fernet</h4>
<p>Fernet es un módulo de <a href="https://es.wikipedia.org/wiki/Criptograf%C3%ADa_sim%C3%A9trica">criptografía simétrica</a>. Garantiza que un mensaje encriptado con este módulo no pueda ser manipulado o leído sin la key.</p>
<pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">cryptography.fernet</span> <span class="k">import</span> <span class="n">Fernet<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">key</span> <span class="o">=</span> <span class="n">Fernet</span><span class="o">.</span><span class="n">generate_key</span><span class="p">()<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span> <span class="o">=</span> <span class="n">Fernet</span><span class="p">(</span><span class="n">key</span><span class="p">)<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">token</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">encrypt</span><span class="p">(</span><span class="sa">b</span><span class="s2">"my deep dark secret"</span><span class="p">)<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">token<br /></span>
<span class="go">'...'<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">decrypt</span><span class="p">(</span><span class="n">token</span><span class="p">)<br /></span>
<span class="go">'my deep dark secret'</span></pre>
<p>También soporta la rotación de keys mediante MultiFernet.</p>
<pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">cryptography.fernet</span> <span class="k">import</span> <span class="n">Fernet</span><span class="p">,</span> <span class="n">MultiFernet<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">key1</span> <span class="o">=</span> <span class="n">Fernet</span><span class="p">(</span><span class="n">Fernet</span><span class="o">.</span><span class="n">generate_key</span><span class="p">())<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">key2</span> <span class="o">=</span> <span class="n">Fernet</span><span class="p">(</span><span class="n">Fernet</span><span class="o">.</span><span class="n">generate_key</span><span class="p">())<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span> <span class="o">=</span> <span class="n">MultiFernet</span><span class="p">([</span><span class="n">key1</span><span class="p">,</span> <span class="n">key2</span><span class="p">])<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">token</span> <span class="o">=</span> <span class="n">f</span><span class="o">.</span><span class="n">encrypt</span><span class="p">(</span><span class="sa">b</span><span class="s2">"Secret message!"</span><span class="p">)<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">token<br /></span>
<span class="go">'...'<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">f</span><span class="o">.</span><span class="n">decrypt</span><span class="p">(</span><span class="n">token</span><span class="p">)<br /></span>
<span class="go">'Secret message!'</span></pre>
<p>Es posible usar contraseñas con Fernet pasándolas por funciones como <a href="https://en.wikipedia.org/wiki/PBKDF2">PBKDF2</a>, o <a href="https://en.wikipedia.org/wiki/Scrypt">Scrypt</a>. </p>
<p>La principal limitación de Fernet es su dificultad a la hora de securizar grandes archivos.</p>
<h4>X.509</h4>
<p>Los certificados X.509 se usan para autentificar clientes y servidores. Normalmente para servidores que usan HTTPS.</p>
<h5>Crear una solicitud de firma de certificado (CSR)</h5>
<p>El CSR es un mensaje enviado por un solicitante a una <a href="https://es.wikipedia.org/wiki/Autoridad_de_certificaci%C3%B3n">autoridad de certificación</a>, para solicitar un <a href="https://es.wikipedia.org/wiki/Certificado_digital">certificado digital</a>. Normalmente contiene la clave pública mediante la cual se referirá al certificado, información identificativa (como el nombre del dominio), o protección de integridad (como la firma digital).</p>
<p>Para obtenerlo, los pasos a seguir suelen ser:</p>
<ol>
<li>Generar una clave privada y una pública</li>
<li>Crear una petición para un certificado, que va firmado por tu clave para demostrar que te pertenece</li>
<li>Entregar el certificado a la autoridad de certificación (SOLO con la pública)</li>
<li>La autoridad reconoce que te pertenece el recurso para el que quieres el certificado</li>
<li>La autoridad te da el certificado firmado por ellos, que identifica tu clave pública y el recurso que has autenticado</li>
<li>Configuras tu servidor para usar ese certificado, combinado con tu clave privada para el tráfico del servidor</li>
</ol>
<p>El código para generar la key privada es el siguiente:</p>
<pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">cryptography.hazmat.backends</span> <span class="kn">import</span> <span class="n">default_backend<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">cryptography.hazmat.primitives</span> <span class="kn">import</span> <span class="n">serialization<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">cryptography.hazmat.primitives.asymmetric</span> <span class="kn">import</span> <span class="n">rsa<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># Generate our key<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">key</span> <span class="o">=</span> <span class="n">rsa</span><span class="o">.</span><span class="n">generate_private_key</span><span class="p">(<br /></span>
<span class="gp">... </span>    <span class="n">public_exponent</span><span class="o">=</span><span class="mi">65537</span><span class="p">,<br /></span>
<span class="gp">... </span>    <span class="n">key_size</span><span class="o">=</span><span class="mi">2048</span><span class="p">,<br /></span>
<span class="gp">... </span>    <span class="n">backend</span><span class="o">=</span><span class="n">default_backend</span><span class="p">()<br /></span>
<span class="gp">... </span><span class="p">)<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># Write our key to disk for safe keeping<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"path/to/store/key.pem"</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:<br /></span>
<span class="gp">... </span>    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">key</span><span class="o">.</span><span class="n">private_bytes</span><span class="p">(<br /></span>
<span class="gp">... </span>        <span class="n">encoding</span><span class="o">=</span><span class="n">serialization</span><span class="o">.</span><span class="n">Encoding</span><span class="o">.</span><span class="n">PEM</span><span class="p">,<br /></span>
<span class="gp">... </span>        <span class="n">format</span><span class="o">=</span><span class="n">serialization</span><span class="o">.</span><span class="n">PrivateFormat</span><span class="o">.</span><span class="n">TraditionalOpenSSL</span><span class="p">,<br /></span>
<span class="gp">... </span>        <span class="n">encryption_algorithm</span><span class="o">=</span><span class="n">serialization</span><span class="o">.</span><span class="n">BestAvailableEncryption</span><span class="p">(</span><span class="sa">b</span><span class="s2">"passphrase"</span><span class="p">),<br /></span>
<span class="gp">... </span>    <span class="p">))</span></pre>
<p>Para la petición de la firma del certificado necesitamos escribir el siguiente código con algunos detalles como nuestra clave pública, información sobre nosotros, e información para qué dominios es el certificado.</p>
<pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">cryptography</span> <span class="kn">import</span> <span class="n">x509<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">cryptography.x509.oid</span> <span class="kn">import</span> <span class="n">NameOID<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">cryptography.hazmat.primitives</span> <span class="kn">import</span> <span class="n">hashes<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># Generate a CSR<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">csr</span> <span class="o">=</span> <span class="n">x509</span><span class="o">.</span><span class="n">CertificateSigningRequestBuilder</span><span class="p">()</span><span class="o">.</span><span class="n">subject_name</span><span class="p">(</span><span class="n">x509</span><span class="o">.</span><span class="n">Name</span><span class="p">([<br /></span>
<span class="gp">... </span>    <span class="c1"># Provide various details about who we are.<br /></span>
<span class="gp">... </span>    <span class="n">x509</span><span class="o">.</span><span class="n">NameAttribute</span><span class="p">(</span><span class="n">NameOID</span><span class="o">.</span><span class="n">COUNTRY_NAME</span><span class="p">,</span> <span class="sa">u</span><span class="s2">"US"</span><span class="p">),<br /></span>
<span class="gp">... </span>    <span class="n">x509</span><span class="o">.</span><span class="n">NameAttribute</span><span class="p">(</span><span class="n">NameOID</span><span class="o">.</span><span class="n">STATE_OR_PROVINCE_NAME</span><span class="p">,</span> <span class="sa">u</span><span class="s2">"CA"</span><span class="p">),<br /></span>
<span class="gp">... </span>    <span class="n">x509</span><span class="o">.</span><span class="n">NameAttribute</span><span class="p">(</span><span class="n">NameOID</span><span class="o">.</span><span class="n">LOCALITY_NAME</span><span class="p">,</span> <span class="sa">u</span><span class="s2">"San Francisco"</span><span class="p">),<br /></span>
<span class="gp">... </span>    <span class="n">x509</span><span class="o">.</span><span class="n">NameAttribute</span><span class="p">(</span><span class="n">NameOID</span><span class="o">.</span><span class="n">ORGANIZATION_NAME</span><span class="p">,</span> <span class="sa">u</span><span class="s2">"My Company"</span><span class="p">),<br /></span>
<span class="gp">... </span>    <span class="n">x509</span><span class="o">.</span><span class="n">NameAttribute</span><span class="p">(</span><span class="n">NameOID</span><span class="o">.</span><span class="n">COMMON_NAME</span><span class="p">,</span> <span class="sa">u</span><span class="s2">"mysite.com"</span><span class="p">),<br /></span>
<span class="gp">... </span><span class="p">]))</span><span class="o">.</span><span class="n">add_extension</span><span class="p">(<br /></span>
<span class="gp">... </span>    <span class="n">x509</span><span class="o">.</span><span class="n">SubjectAlternativeName</span><span class="p">([<br /></span>
<span class="gp">... </span>        <span class="c1"># Describe what sites we want this certificate for.<br /></span>
<span class="gp">... </span>        <span class="n">x509</span><span class="o">.</span><span class="n">DNSName</span><span class="p">(</span><span class="sa">u</span><span class="s2">"mysite.com"</span><span class="p">),<br /></span>
<span class="gp">... </span>        <span class="n">x509</span><span class="o">.</span><span class="n">DNSName</span><span class="p">(</span><span class="sa">u</span><span class="s2">"www.mysite.com"</span><span class="p">),<br /></span>
<span class="gp">... </span>        <span class="n">x509</span><span class="o">.</span><span class="n">DNSName</span><span class="p">(</span><span class="sa">u</span><span class="s2">"subdomain.mysite.com"</span><span class="p">),<br /></span>
<span class="gp">... </span>    <span class="p">]),<br /></span>
<span class="gp">... </span>    <span class="n">critical</span><span class="o">=</span><span class="bp">False</span><span class="p">,<br /></span>
<span class="gp">... </span><span class="c1"># Sign the CSR with our private key.<br /></span>
<span class="gp">... </span><span class="p">)</span><span class="o">.</span><span class="n">sign</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">hashes</span><span class="o">.</span><span class="n">SHA256</span><span class="p">(),</span> <span class="n">default_backend</span><span class="p">())<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># Write our CSR out to disk.<br /></span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"path/to/csr.pem"</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:<br /></span>
<span class="gp">... </span>    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">csr</span><span class="o">.</span><span class="n">public_bytes</span><span class="p">(</span><span class="n">serialization</span><span class="o">.</span><span class="n">Encoding</span><span class="o">.</span><span class="n">PEM</span><span class="p">))</span></pre>
<p>Ya solo quedaría dar nuestra petición a la autoridad de certificación para que nos devuelva el certificado.</p>

<h3>Otras funciones</h3>
<p>Lo que viene aquí corresponde al módulo de "Materiales peligrosos". SOLO debe usarse si se está seguro al 100% de lo que se está haciendo, porque este módulo (según su página web oficial), está lleno de "minas, dragones, y dinosaurios con pistolas láser".</p>
<h4>Primitivos</h4>
<p>Son algoritmos de bajo nivel usados para construir protocolos criptográficos para sistemas de seguridad informática.</p>
<h4>Excepciones</h4>
<p>Este módulo cuenta con distintas excepciones como "UnsupportedAlgorithm", que se le llama cuando un algoritmo no es soportado por Cryptography, "AlreadyFinalized", para cuando se usa un contexto ya finalizado, "InvalidSignature", cuando la verificación de la firma digital falla, y algunas<a href="https://cryptography.io/en/latest/exceptions/"> más</a></p>
<h4>Generación de números aleatorios</h4>
<p>Cuando se generan datos aleatorios para usar en operaciones criptográficas, no es recomendable usar un módulo "random" estándar, ya que no tienen un generador de números aleatorios securizado criptográficamente. Por lo tanto, se recomienda el uso del generador de números aleatorios del propio sistema operativo "os.urandom()"</p>
<h4>Backends</h4>
<p>Cryptography fue diseñado para soportar múltiples backends, pero actualmente este diseño ha sido deprecado. Se puede obtener el backend por defecto llamando a "default_backend()"</p>

<h3>Proyecto</h3>
<h4>Ejemplo simple</h4>
<p><a href="https://pastebin.com/iRdzYJGT" rel="noreferrer" target="_blank">https://pastebin.com/iRdzYJGT</a></p>
<h4>Ejemplo contraseñas</h4>
<p><a href="https://pastebin.com/bmrisiii">https://pastebin.com/bmrisiii</a></p>
