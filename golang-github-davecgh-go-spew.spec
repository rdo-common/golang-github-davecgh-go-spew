%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         davecgh
%global repo            go-spew
%global import_path     %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          3e6e67c4dcea3ac2f25fd4731abc0e1deaf36216
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.3.git%{shortcommit}%{?dist}
Summary:        Implements a deep pretty printer for Go data structures to aid in debugging
License:        ISC
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}/spew) = %{version}-%{release}
Provides:       golang(%{import_path}/spew/testdata) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for 
building other packages which use %{project}/%{repo}.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav spew %{buildroot}/%{gopath}/src/%{import_path}/

%check
# NOTE in spew/testdata/dumpcgo.go
#GOPATH={buildroot}/{gopath}:{gopath} go test {import_path}/spew

%files devel
%doc README.md LICENSE
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}

%changelog
* Mon Apr 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git3e6e67c
- Bump to upstream 3e6e67c4dcea3ac2f25fd4731abc0e1deaf36216
  related: #1172198

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git1aaf839
- Bump to upstream 1aaf839fb07e099361e445273993ccd9adc21b07
  related: #1172198

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.git83f84dc
- First package for Fedora
  resolves: #1172198
