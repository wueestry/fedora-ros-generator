# Meta Package
Name:           ros-jazzy-libcurl-vendor
Version:        3.4.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/curl/curl
Summary:        Meta package for ros2-jazzy-libcurl_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-libcurl_vendor
Requires:       ros2-jazzy-libcurl_vendor-devel

Obsoletes: ros-jazzy-libcurl-vendor < 3.4.3-1

%description
Wrapper around libcurl, it provides a fixed CMake module and an
ExternalProject build of it.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.3-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.4.1-1
- Update to latest release
