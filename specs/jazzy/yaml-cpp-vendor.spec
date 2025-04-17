# Meta Package
Name:           ros-jazzy-yaml-cpp-vendor
Version:        9.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/jbeder/yaml-cpp
Summary:        Meta package for ros2-jazzy-yaml_cpp_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-yaml_cpp_vendor
Requires:       ros2-jazzy-yaml_cpp_vendor-devel

Obsoletes: ros-jazzy-yaml-cpp-vendor < 9.0.1-1

%description
Wrapper around yaml-cpp, it provides a fixed CMake module and an
ExternalProject build of it.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.0.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.0.0-1
- Update to latest release
