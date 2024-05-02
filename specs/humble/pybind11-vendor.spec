# Meta Package
Name:           ros-humble-pybind11-vendor
Version:        2.4.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/pybind/pybind11
Summary:        Meta package for ros2-humble-pybind11_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-pybind11_vendor
Requires:       ros2-humble-pybind11_vendor-devel

Obsoletes: ros-humble-pybind11-vendor < 2.4.2-1

%description
Wrapper around pybind11.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.2-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.2-1
- Initial humble build
