%define		plugin		w3pw
Summary:	DokuWiki W3PW Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	0.2
Release:	3
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/glensc/dokuwiki-plugin-w3pw/archive/refs/tags/2011-11-23.tar.gz
# Source0-md5:	dba22dc4e0ff04997b2f6eeccc1e8d52
URL:		https://github.com/glensc/dokuwiki-plugin-w3pw
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20080505
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
This plugin adds markup to link to W3PW passwords.

%prep
%setup -qc
mv dokuwiki-plugin-w3pw-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/LICENSE

# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/syntax.php
%{plugindir}/conf
