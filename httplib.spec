%define major 0
%define devname %mklibname httplib -d

Name:		httplib
Version:	0.42.0
Release:	1
Source0:	https://github.com/yhirose/cpp-httplib/archive/refs/tags/v%{version}.tar.gz
Summary:	Simple C++ HTTP(S) 1.1 Client/Server library
URL:		https://github.com/yhirose/cpp-httplib
License:	MIT
Group:		System/Libraries
BuildArch:	noarch
BuildRequires:	cmake
BuildSystem:	cmake

%description
Simple C++ HTTP(S) 1.1 Client/Server library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Simple C++ HTTP(S) 1.1 Client/Server library

%files -n %{devname}
%doc %{_docdir}/httplib/README.md
%license %{_datadir}/licenses/httplib/LICENSE
%{_includedir}/*
%{_libdir}/cmake/*
