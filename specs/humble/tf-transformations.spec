# Meta Package
Name:           ros-humble-tf-transformations
Version:        1.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-tf_transformations and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tf_transformations
Requires:       ros2-humble-tf_transformations-devel

Obsoletes: ros-humble-tf-transformations < 1.1.0-1

%description
Reimplementation of the tf/transformations.py library for common
Python spatial operations

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.1.0-1
- Update to latest release
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.1-1
- update to latest release
* Sun Jun 18 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.1-1
- update to latest release
