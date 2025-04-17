# Meta Package
Name:           ros-jazzy-pybind11-vendor
Version:        3.1.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/pybind/pybind11
Summary:        Meta package for ros2-jazzy-pybind11_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pybind11_vendor
Requires:       ros2-jazzy-pybind11_vendor-devel

Obsoletes: ros-jazzy-pybind11-vendor < 3.1.3-1

%description
Wrapper around pybind11.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.2-1
- Update to latest release
