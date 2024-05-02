# Meta Package
Name:           ros-humble-pcl-conversions
Version:        2.4.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-pcl_conversions and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-pcl_conversions
Requires:       ros2-humble-pcl_conversions-devel

Obsoletes: ros-humble-pcl-conversions < 2.4.0-1

%description
Provides conversions from PCL data types and ROS message types

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 25 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.0-1
- Update to latest release
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.3-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.0-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.4.0-1
- Initial humble build
