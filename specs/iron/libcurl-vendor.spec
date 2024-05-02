# Meta Package
Name:           ros-iron-libcurl-vendor
Version:        3.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/curl/curl
Summary:        Meta package for ros2-iron-libcurl_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-libcurl_vendor
Requires:       ros2-iron-libcurl_vendor-devel

Obsoletes: ros-iron-libcurl-vendor < 3.2.2-1

%description
Wrapper around libcurl, it provides a fixed CMake module and an
ExternalProject build of it.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.2.2-1
- Update to latest release
