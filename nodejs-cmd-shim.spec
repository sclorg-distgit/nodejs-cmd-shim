%{?scl:%scl_package nodejs-cmd-shim}
%{!?scl:%global pkg_name %{name}}

%{!?scl:%global enable_tests 1}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-cmd-shim
Version:        2.0.0
Release:        2%{?dist}
Summary:        Used to create executable scripts on Windows and Unix
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch
License:        BSD
URL:            https://github.com/ForbesLindesay/cmd-shim
Source0:        http://registry.npmjs.org/cmd-shim/-/cmd-shim-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(rimraf)
%endif

%description
The cmd-shim used in npm to create executable scripts on Windows, since symlinks
are not suitable for this purpose there.

On Unix systems, you should use a symbolic link instead, but this module
supports creating shell script shims also.

%prep
%setup -q -n package

# CRLF -> LF
sed -i 's/\r//g' README.md LICENSE

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cmd-shim
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/cmd-shim

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%tap test/*.js
%endif

%files
%{nodejs_sitelib}/cmd-shim
%doc README.md LICENSE

%changelog
* Wed Jul 15 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-2
- Enable tests
- minor changes

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-1
- New upstream release 2.0.0

* Thu Nov 07 2013 Tomas Hrcka <thrcka@redhat.com> - 1.1.0-4.1
- Software collections support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-3
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2
- fix EOL encodings

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-1
- initial package
