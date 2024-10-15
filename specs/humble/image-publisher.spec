# Meta Package
Name:           ros-humble-image-publisher
Version:        3.0.5
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/image_publisher/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-humble-image_publisher and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_publisher
Requires:       ros2-humble-image_publisher-devel

Obsoletes: ros-humble-image-publisher < 3.0.5-1

%description
Contains a node publish an image stream from single image file or avi
motion file.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.5-1
- Update to latest release
