# ---+ LDAP settings
# This is the configuration used by the <b>LdapContrib</b> and the
# <b>LdapNgPlugin</b>. 
# <p>
# To use an LDAP server for authentication you have to use the PasswordManager
# <b>LdapPasswdUser</b>.
# To Use groups defined in LDAP enable the UserMappingManager <b>LdapUserMapping</b>.
# (see the Security Setting section)

# <h2>Connection settings</h2>

# **STRING**
# IP address (or hostname) of the LDAP server
$Foswiki::cfg{Ldap}{Host} = 'my.domain.com';

# **NUMBER**
# Port used when binding to the LDAP server
$Foswiki::cfg{Ldap}{Port} = 389;

# **NUMBER**
# Ldap protocol version to use when querying the server; 
# Possible values are: 2, 3
$Foswiki::cfg{Ldap}{Version} = '3';

# **STRING**
# Base DN to use in searches
$Foswiki::cfg{Ldap}{Base} = 'dc=my,dc=domain,dc=com';

# **STRING**
# The DN to use when binding to the LDAP server; if undefined anonymous binding
# will be used. Example 'cn=proxyuser,dc=my,dc=domain,dc=com'
$Foswiki::cfg{Ldap}{BindDN} = '';

# **PASSWORD**
# The password used when binding to the LDAP server
$Foswiki::cfg{Ldap}{BindPassword} = 'secret';

# **BOOLEAN**
# Use SASL authentication when binding to the server; Note, when using SASL the 
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{Ldap}{UseSASL} = 0;

# **STRING**
# List of SASL authentication mechanism to try; defaults to 'PLAIN CRAM-MD5
# EXTERNAL ANONYMOUS'
$Foswiki::cfg{Ldap}{SASLMechanism} = 'PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **BOOLEAN**
# Use Transort Layer Security (TLS) to encrypt the connection to the LDAP server.
# You will need to specify the servers CA File using the TLSCAFile option
$Foswiki::cfg{Ldap}{UseTLS} = 0;

# **STRING**
# This defines the version of the SSL/TLS protocol to use. Possible values are:
# 'sslv2', 'sslv3',  'sslv2/3' or 'tlsv1'
$Foswiki::cfg{Ldap}{TLSSSLVersion} = 'tlsv1';

# **STRING**
# Specify how to verify the servers certificate. Possible values are: 'require', 'optional'
# or 'require'.
$Foswiki::cfg{Ldap}{TLSVerify} = 'require';

# **STRING**
# Pathname of the directory containing CA certificates
$Foswiki::cfg{Ldap}{TLSCAPath} = '';

# **STRING**
# Filename containing the certificate of the CA which signed the server’s certificate.
$Foswiki::cfg{Ldap}{TLSCAFile} = '';

# **STRING**
# Client side certificate file
$Foswiki::cfg{Ldap}{TLSClientCert} = '';

# **STRING**
# Client side private key file
$Foswiki::cfg{Ldap}{TLSClientKey} = '';

# **BOOLEAN**
# Enable/disable debug output to STDERR. This will end up in your web server's log files.
# But you are adviced to redirect STDERR of the wiki engine to a separate file. This can be done by
# commenting out the prepaired command in the <code>lib/Foswiki/UI.pm</code> file. See the 
# comments there.
$Foswiki::cfg{Ldap}{Debug} = 0;

# **STRING**
# <h2>User settings</h2>
# The options below configure how the wiki will extract account records from LDAP.
#
# <!-- work around broken configure -->
# </td></tr><tr><td colspan="2" class="docdata info">
#
# The distinguished name of the users tree. All user accounts will
# be searched for in the subtree under UserBase.
$Foswiki::cfg{Ldap}{UserBase} = 'ou=people,dc=my,dc=domain,dc=com';

# **STRING**
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{Ldap}{LoginFilter} = 'objectClass=posixAccount';

# **STRING**
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{Ldap}{LoginAttribute} = 'uid';

# **STRING**
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from. 
$Foswiki::cfg{Ldap}{WikiNameAttribute} = 'cn';

# **BOOLEAN**
# Enable/disable normalization of WikiUserNames as they come from LDAP
# If the WikiNameAttribute is set to 'mail' a trailing @my.domain.com
# is stripped. WARNING: if you switch this off you have to garantee that the WikiNames
# in the WikiNameAttribute are a proper WikiWord (camel-case, no spaces, no umlauts etc).
$Foswiki::cfg{Ldap}{NormalizeWikiNames} = 1;

# **BOOLEAN**
# Enable/disable normalization of login names
$Foswiki::cfg{Ldap}{NormalizeLoginNames} = 0;

# **STRING**
# Alias old !WikiNames to new account. This is a comma separated list of
# "OldName=NewName" values.
$Foswiki::cfg{Ldap}{WikiNameAliases} = '';

# **BOOLEAN**
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{Ldap}{AllowChangePassword} = 0;

# **SELECTCLASS none,Foswiki::Users::*User**
# Define a secondary password manager used to authenticate users that are 
# registered to the wiki natively. Note, that <b>this must not be Foswiki::Users::LdapPasswdUser again!</b>
$Foswiki::cfg{Ldap}{SecondaryPasswordManager} = 'none';

# **STRING**
# <h2>Group settings</h2>
# The settings below configures the mapping and processing of LoginNames and WikiNames as
# well as the use of LDAP groups. 
# In any case you have to select the LdapUserMapping as the UserMappingManager in the
# Security Section section above.
#
# <!-- work around broken configure -->
# </td></tr><tr><td colspan="2" class="docdata info">
#
# The distinguished name of the groups tree. All group definitions
# are used in the subtree under GroupBase. 
$Foswiki::cfg{Ldap}{GroupBase} = 'ou=group,dc=my,dc=domain,dc=com';

# **STRING**
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{Ldap}{GroupFilter} = 'objectClass=posixGroup';

# **STRING**
# This is the name of the attribute that holds the name of the 
# group in a group record.
$Foswiki::cfg{Ldap}{GroupAttribute} = 'cn';

# **STRING**
# This is the name of the attribute that holds the primary group attribute.
# This attribute is stored as part of the user record and refers to the
# primary group this user is in. Sometimes, this membership is not captured
# in the group record itself but in the user record to make it the primary group
# a user is in.
$Foswiki::cfg{Ldap}{PrimaryGroupAttribute} = 'gidNumber';

# **STRING**
# The attribute that should be used to collect group members. This is the name of the
# attribute in a group record used to point to the user record. For example, in a possix setting this
# is the uid of the relevant posixAccount. If groups are implemented using the object class
# 'groupOfNames' the MemberAttribute will store a literal DN pointing to the account record. In this
# case you have to switch on the MemberIndirection flag below.
$Foswiki::cfg{Ldap}{MemberAttribute} = 'memberUid';

# **BOOLEAN**
# Flag indicating wether the MemberAttribute of a group stores a DN. 
$Foswiki::cfg{Ldap}{MemberIndirection} = 0;

# **BOOLEAN**
# Flag indicating wether we fallback to WikiGroups. If this is switched on, 
# standard Wiki groups will be used as a fallback if a group definition of a given
# name was not found in the LDAP database.
$Foswiki::cfg{Ldap}{WikiGroupsBackoff} = 1;

# **BOOLEAN**
# Enable/disable normalization of group names as they come from LDAP:
$Foswiki::cfg{Ldap}{NormalizeGroupNames} = 0;

# **BOOLEAN**
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{Ldap}{MapGroups} = 1;

# **NUMBER** 
# <h2>Performance settings</h2>
# The following settings are used to optimize performance in your environment. Please take care.
#
# <!-- work around broken configure -->
# </td></tr><tr><td colspan="2" class="docdata info">
#
# Time in seconds when cache data expires and is reloaded anew, defaults to one day.
$Foswiki::cfg{Ldap}{MaxCacheAge} = 86400;

# **NUMBER**
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
$Foswiki::cfg{Ldap}{PageSize} = 500; 

# **STRING 50**
# Prevent certain names from being looked up in LDAP
$Foswiki::cfg{Ldap}{Exclude} = 'WikiGuest, FoswikiContributor, ProjectContributor, RegistrationAgent, AdminGroup, NobodyGroup';
