# ---+ Extensions
# ---++ LDAP 
# This is the configuration used by the <b>LdapContrib</b> and the
# <b>LdapNgPlugin</b>.
# <p>
# To use an LDAP server for authentication you have to use the PasswordManager
# <b>LdapPasswdUser</b>.
# To Use groups defined in LDAP enable the UserMappingManager <b>LdapUserMapping</b>.
# (see the Security Setting section)

# ---+++ Connection settings

# **STRING**
# IP address (or hostname) of the LDAP server
$Foswiki::cfg{Ldap}{Host} = 'ldap.my.domain.com';

# **NUMBER**
# Port used when binding to the LDAP server
$Foswiki::cfg{Ldap}{Port} = 389;

# **BOOLEAN**
# Switch on this flag to enable IPv6 support when connecting to the LDAP server. 
# Note that IPv6+SSL is still considered experimental. When disabled a normal IPv4 connection is established.
# To make use of this feature you require IO::Socket::INET6.
$Foswiki::cfg{Ldap}{IPv6} = 0;

# **NUMBER**
# Ldap protocol version to use when querying the server;
# Possible values are: 2, 3
$Foswiki::cfg{Ldap}{Version} = 3;

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

# **STRING**
# Path to keytab of this server. This is used for Kerberos single sign on. Note that you will have to 
# Switch the {LoginManager} to <code>KerberosLogin</code> to make use of this feature.
# Note also that this keytab must have a HTTP/mydomain.com principal name assigned to it.
$Foswiki::cfg{Ldap}{KerberosKeyTab} = '/etc/krb5.keytab';

# **STRING**
# Set this to the charset encoding of data coming from the LDAP server.
# Normally this should be 'utf-8', but might differ in some cases.
# Data read from the server will then be converted from this encoding
# and translated to your site's charset encoding as configured in <code>{Site}{CharSet}</code>.
# WARNING: if you change the charset encoding after having used a different one for some time
# you will require to remove all cached data in <code>.../working/work_areas/LdapContrib</code>
# and <code>.../working/work_areas/LdapNgPlugin/cache</code>. Otherwise this data 
# will be reused assuming a false charset encoding.
$Foswiki::cfg{Ldap}{CharSet} = 'utf-8';

# **BOOLEAN**
# Use SASL authentication when binding to the server; Note, when using SASL the
# BindDN and BindPassword setting are used to configure the SASL access.
$Foswiki::cfg{Ldap}{UseSASL} = 0;

# **STRING**
# List of SASL authentication mechanism to try; defaults to 'PLAIN CRAM-MD5
# EXTERNAL ANONYMOUS'
$Foswiki::cfg{Ldap}{SASLMechanism} = 'PLAIN CRAM-MD5 EXTERNAL ANONYMOUS';

# **STRING**
# If the GSSAPI mechanism is used in {Ldap}{SASLMechanism}, and the underlying
# implementation is MIT Kerberos 5, this setting can be used to override the
# ticket cache file to be used.
$Foswiki::cfg{Ldap}{Krb5CredentialsCacheFile} = '';

# **PERL**
# Add a key for each LDAP referral link to supply a hashref with configuration
# overrides for the referral target. This can be used to override auth
# mechanisms and credentials. Please note that for technical reasons the keys
# in the hashref have to match the internal keys of the LdapContrib object
# rather than the keys in this configuration.
# The following is a list of relevant keys: host, base, port, ipv6, bindDN,
# bindPassword, useSASL, saslMechanism, krb5CredCache, useTLS, tlsVerify,
# tlsSSLVersion, tlsCAFile, tlsCAPath, tlsClientCert, tlsClientKey
$Foswiki::cfg{Ldap}{ReferralConfig} = {};

# **BOOLEAN**
# If you enable this, referrals from an LDAP server will be ignored unless the
# referral URL is present as a key in {Ldap}{ReferralConfig}. This avoids
# following referrals for data that is not actually needed.
$Foswiki::cfg{Ldap}{KnownReferralsOnly} = 0;

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

# ---+++ User settings
# The options below configure how the wiki will extract account records from LDAP.

# **PERL**
# A list of trees where to search for users records. 
$Foswiki::cfg{Ldap}{UserBase} = ['ou=people,dc=my,dc=domain,dc=com'];

# **STRING**
# Filter to be used to find login accounts. Compare to GroupFilter below
$Foswiki::cfg{Ldap}{LoginFilter} = 'objectClass=person';

# **SELECT sub,one**
# The scope of the search for users starting at UserBase. While "sub" search recursively
# a "one" will only search up to one level under the UserBase.
$Foswiki::cfg{Ldap}{UserScope} = 'sub';

# **STRING**
# The user login name attribute. This is the attribute name that is
# used to login.
$Foswiki::cfg{Ldap}{LoginAttribute} = 'sAMAccountName';

# **STRING**
# The user mail attribute. This is the attribute name used to fetch
# users e-mail.
$Foswiki::cfg{Ldap}{MailAttribute} = 'mail';

# **STRING**
# Comma-separated list of extra fields to cache (as a JSON object) for display
# purposes.
$Foswiki::cfg{Ldap}{DisplayAttributes} = 'displayName';

# **STRING**
# Formatting string for generating a "display name" (human-friendly label for a user).
# You can use $x to refer to the value of field x, but only if it is imported
# using {Ldap}{DisplayAttributes}.
# Additionally, you can use the following syntax: $x(pre|post|alt)
# In case there is a value for the field, 'pre' will be prepended and 'post' will be appended.
# 'alt' will be used for the value, without 'pre' and 'post', if no value exists for the user.
$Foswiki::cfg{Ldap}{DisplayNameFormat} = '$displayName';

# **STRING**
# The user's wiki name attribute. This is the attribute to generate
# the WikiName from.
$Foswiki::cfg{Ldap}{WikiNameAttributes} = 'givenName,sn';

# **BOOLEAN**
# Enable/disable normalization of WikiUserNames as they come from LDAP
# If the WikiNameAttribute is set to 'mail' a trailing @my.domain.com
# is stripped. WARNING: if you switch this off you have to garantee that the WikiNames
# in the WikiNameAttribute are a proper WikiWord (camel-case, no spaces, no umlauts etc).
$Foswiki::cfg{Ldap}{NormalizeWikiNames} = 1;

# **BOOLEAN**
# Enable/disable normalization of login names
$Foswiki::cfg{Ldap}{NormalizeLoginNames} = 0;

# **BOOLEAN**
# Enable/disable case sensitive login names. If disabled case doesn't matter while logging in.
$Foswiki::cfg{Ldap}{CaseSensitiveLogin} = 0;

# **STRING**
# Alias old !WikiNames to new account. This is a comma separated list of
# "OldName=NewName" values.
# Warning: this setting is deprecated - use <code>RewriteWikiNames</code> instead
$Foswiki::cfg{Ldap}{WikiNameAliases} = '';

# **PERL**
# A hash mapping of rewrite rules. Rules are separated by commas. A rule has
# the form
# <pre>{
#   'pattern1' => 'substitute1',
#   'pattern2' => 'substitute2'
# }</pre>
# consists of a name pattern that has to match the wiki name to be rewritten
# and a substitute value that is used to replace the matched pattern. The
# substitute might contain $1, $2, ... , $5 to insert the first, second, ..., fifth
# bracket pair in the key pattern. (see perl manual for regular expressions).
# Example: '(.*)_users' => '$1'
$Foswiki::cfg{Ldap}{RewriteWikiNames} = { '^(.*)@.*$' => '$1' };

# **PERL**
# A mapping of rewrite rules. Works just like the previous setting, but
# now applies to login names. This might be useful for migrating to a different
# structure of the underlying authentication database. Rules are applied in
# order; rewriting stops after the first rules matches. Rules have the form
# <pre>[
#   ['pattern1' => 'substitute1',
#   ['pattern2' => 'substitute2'
# ]</pre>
$Foswiki::cfg{Ldap}{RewriteLoginNames} = [];

# **BOOLEAN**
# Allow/disallow changing the LDAP password using the ChangePassword feature
$Foswiki::cfg{Ldap}{AllowChangePassword} = 0;

# **STRING**
# This parameter allows to hard-code a LoginName-to-WikiName mapping in a wiki topic. This 
# feature may be used to migrate from a TopicUserMapping to LdapUserMapping by preserving any already existing
# mapping stored in Main.WikiUsers. Leave it empty to disable this feature and build WikiNames by reading
# LDAP attributes as normal.
$Foswiki::cfg{Ldap}{UserMappingTopic} = '';

# ---+++ Group settings
# The settings below configures the mapping and processing of LoginNames and WikiNames as
# well as the use of LDAP groups.
# In any case you have to select the LdapUserMapping as the UserMappingManager in the
# Security Section section above.

# **PERL**
# A list of trees where to search for group records.
$Foswiki::cfg{Ldap}{GroupBase} = ['ou=group,dc=my,dc=domain,dc=com'];

# **STRING**
# Filter to be used to find groups. Compare to LoginFilter.
$Foswiki::cfg{Ldap}{GroupFilter} = 'objectClass=group';

# **SELECT sub,one**
# The scope of the search for groups starting at GroupBase. While "sub" search recursively
# a "one" will only search up to one level under the GroupBase.
$Foswiki::cfg{Ldap}{GroupScope} = 'sub';

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
$Foswiki::cfg{Ldap}{MemberAttribute} = 'member';

# **STRING**
# This is the name of the attribute in a group record used to point to the inner group record.
# This value is often the same than MemberAttribute but may differ for some LDAP servers.
$Foswiki::cfg{Ldap}{InnerGroupAttribute} = 'member';

# **BOOLEAN**
# Flag indicating wether the MemberAttribute of a group stores a DN.
$Foswiki::cfg{Ldap}{MemberIndirection} = 1;

# **BOOLEAN**
# Flag indicating wether we fallback to WikiGroups. If this is switched on,
# standard Wiki groups will be used as a fallback if a group definition of a given
# name was not found in the LDAP database.
$Foswiki::cfg{Ldap}{WikiGroupsBackoff} = 1;

# **BOOLEAN**
# Enable/disable normalization of group names as they come from LDAP:
$Foswiki::cfg{Ldap}{NormalizeGroupNames} = 0;

# **BOOLEAN**
# Enable/disable generation of "private groups". Some posix systems generate a
# group for each user account with the same name like the user account. These groups have a
# single member, the user itself. As these groups don't really make sense to have in Foswik,
# this flag is disabled by default.
$Foswiki::cfg{Ldap}{IgnorePrivateGroups} = 1;

# **BOOLEAN**
# Enable use of LDAP groups. If you switch this off the group-related settings
# have no effect. This flag is of use if you don't want to define groups in LDAP
# but still want to map LoginNames to WikiNames on the base of LDAP data.
$Foswiki::cfg{Ldap}{MapGroups} = 1;

# **PERL**
# A hash mapping of rewrite rules. Rules are separated by commas. A rule has
# the form
# <pre>{
#   'pattern1' => 'substitute1',
#   'pattern2' => 'substitute2'
# }</pre>
# consists of a name pattern that has to match the group name to be rewritten
# and a substitute value that is used to replace the matched pattern. The
# substitute might contain $1, $2, ... , $5 to insert the first, second, ..., fifth
# bracket pair in the key pattern. (see perl manual for regular expressions).
# Example: '(.*)_users' => '$1'
$Foswiki::cfg{Ldap}{RewriteGroups} = {
};

# **PERL**
# A hash mapping of group ID associations. Rules are separated by commas. A rule has
# the form
# <pre>{
#   'group1' => 'primaryGroupId1',
#   'group2' => 'primaryGroupId2'
# }</pre>
# Example: 'CN=Domain Users,CN=Builtin,DC=example,DC=com' => '513'
$Foswiki::cfg{Ldap}{PrimaryGroupMapping} = {};

# **BOOLEAN**
# Flag indicating if groups that get the same are merged. For exmaple, given two
# ldap groups end up having the same name even though they have a different distinguished name
# or have been rewritten to match on the same group name (see RewriteGroups), then members
# of both groups are merged into one group of that name.
$Foswiki::cfg{Ldap}{MergeGroups} = 0;

# ---+++ Performance settings
# The following settings are used to optimize performance in your environment. Please take care.

# **NUMBER**
# Time in seconds when cache data expires and is reloaded anew, defaults to one day.
$Foswiki::cfg{Ldap}{MaxCacheAge} = 86400;

# **BOOLEAN**
# Enable precaching of LDAP data. If you switch this off the LDAP users and groups will not be
# prefetched from LDAP when building a new cache. Activated by default.
$Foswiki::cfg{Ldap}{Precache} = 1;

# **NUMBER**
# Number of user objects to fetch in one paged result when building the username mappings;
# this is a speed optimization option, use this value with caution.
# Requires access to the 'control' LDAP extension as an LDAP client. Use '0' to disable it.
$Foswiki::cfg{Ldap}{PageSize} = 500;

# **STRING 50**
# Prevent certain names from being looked up in LDAP
$Foswiki::cfg{Ldap}{Exclude} = 'WikiGuest, ProjectContributor, RegistrationAgent, UnknownUser, AdminGroup, NobodyGroup, AdminUser, admin, guest';

1;
