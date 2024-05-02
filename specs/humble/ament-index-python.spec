# Meta Package
Name:           ros-humble-ament-index-python
Version:        1.4.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ament_index_python and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ament_index_python
Requires:       ros2-humble-ament_index_python-devel

Obsoletes: ros-humble-ament-index-python < 1.4.0-1

%description
Python API to access the ament resource index.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.4.0-1
- Initial humble build
