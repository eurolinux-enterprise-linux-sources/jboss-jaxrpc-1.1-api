%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxrpc-1.1-api
Version:          1.0.1
Release:          7%{?dist}
Summary:          Java API for XML-Based RPC (JAX-RPC) 1.1
Group:            Development/Libraries
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaxrpc-api_spec.git jboss-jaxrpc-1.1-api
# cd jboss-jaxrpc-1.1-api/ && git archive --format=tar --prefix=jboss-jaxrpc-1.1-api/ jboss-jaxrpc-api_1.1_spec-1.0.1.Final | xz > jboss-jaxrpc-1.1-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    java-devel
BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-ejb-plugin

Requires:         jboss-servlet-3.0-api
Requires:         jpackage-utils
Requires:         java

BuildArch:        noarch

%description
The JAX-RPC 1.1 API classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Libraries
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaxrpc-1.1-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-jaxrpc-api_1.1_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.1-7
- Mass rebuild 2013-12-27

* Fri Dec 13 2013 Ade Lee <alee@redhat.com> 1.0.1-6
- Fix spec file dist tag for rpmlint

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-5
- Remove unneeded BR: maven-plugin-cobertura

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.1-4
- Resolves #961461 - Remove unneeded maven-checkstyle-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.20120309gita3c227
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120309gita3c227
- Packaging after license cleanup upstrea

* Mon Oct 24 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-2
- Fixed apidocs issue

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Initial packaging
