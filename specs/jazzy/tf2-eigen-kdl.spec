# Meta Package
Name:           ros-jazzy-tf2-eigen-kdl
Version:        0.36.9
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tf2_eigen_kdl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tf2_eigen_kdl
Requires:       ros2-jazzy-tf2_eigen_kdl-devel

Obsoletes: ros-jazzy-tf2-eigen-kdl < 0.36.9-1

%description
Conversion functions between: - Eigen and KDL

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.9-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.8-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.7-1
- Update to latest release
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.36.2-1
- Update to latest release
